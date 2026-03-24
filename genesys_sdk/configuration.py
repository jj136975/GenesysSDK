# coding: utf-8

import json
import os
import ssl
import sys
from configparser import ConfigParser, MissingSectionHeaderError
from dataclasses import dataclass, field
from os.path import expanduser
from typing import Any

from aiohttp import ClientSession, TCPConnector

from simple_sdk.config import BaseConfiguration

from .logger import Logger, LogFormat, LogLevel
from .region import PureCloudRegionHosts

ConfigPath = str | bytes | os.PathLike[str] | os.PathLike[bytes]


@dataclass(kw_only=True)
class GenesysConfiguration(BaseConfiguration):
    """Genesys Cloud API configuration."""

    base_url: str = ""
    """API base URL. Auto-set from host if empty."""

    agent: str = 'Genesys Light SDK/python'

    host: PureCloudRegionHosts = PureCloudRegionHosts.eu_central_1
    """Genesys Cloud region."""

    # Retry settings
    retry_delay: float = 3.0
    """Delay in seconds for 202 (Request Not Ready) retries."""

    # Temp file folder for downloading files
    temp_folder_path: str | None = None

    # SSL/TLS verification
    verify_ssl: bool = True
    ssl_ca_cert: str | None = None
    cert_file: str | None = None
    key_file: str | None = None

    # Proxy (uses trust_env=True — set HTTP_PROXY/HTTPS_PROXY env vars)
    proxy: str | None = None
    proxy_username: str | None = None
    proxy_password: str | None = None

    # Gateway
    gateway_configuration: str | None = None

    # Logging
    logger: Logger = field(default_factory=Logger)

    # Config file
    config_file_path: ConfigPath = field(
        default_factory=lambda: os.path.join(expanduser("~"), ".genesyscloudpython", "config")
    )

    def __post_init__(self):
        if not self.base_url:
            self.base_url = self.host.api_host
        self._update_config_from_file()

    def create_session(self, **kwargs: Any) -> ClientSession:
        """Create an aiohttp ClientSession with SSL, proxy, and trace logging configured."""
        kwargs.setdefault('connector', self._create_connector())
        kwargs.setdefault('trace_configs', [self.logger.create_trace_config()])
        kwargs.setdefault('trust_env', True)
        return super().create_session(**kwargs)

    def _create_connector(self) -> TCPConnector:
        """Create a TCPConnector with SSL/TLS configuration."""
        if not self.verify_ssl:
            return TCPConnector(ssl=False)
        if self.ssl_ca_cert or self.cert_file:
            ctx = ssl.create_default_context(cafile=self.ssl_ca_cert)
            if self.cert_file:
                ctx.load_cert_chain(self.cert_file, keyfile=self.key_file)
            return TCPConnector(ssl=ctx)
        return TCPConnector()

    @classmethod
    def to_debug_report(cls) -> str:
        """Gets the essential information for debugging."""
        return f"""\
Python SDK Debug Report:
OS: {sys.platform}
Python Version: {sys.version}
Version of the API: v2
SDK Package Version: 226.0.0"""

    def _update_config_from_file(self):
        try:
            config = ConfigParser()
            try:
                if not config.read(self.config_file_path):
                    return
            except MissingSectionHeaderError:
                try:
                    with open(self.config_file_path, "r") as read_file:
                        config = json.load(read_file)
                except Exception as e:
                    print("[Error] Could not read config file:", e)
                    return

            # logging
            log_level = _get_config_string(config, "logging", "log_level")
            if log_level is not None:
                self.logger.log_level = LogLevel.from_string(log_level)

            log_format = _get_config_string(config, "logging", "log_format")
            if log_format is not None:
                self.logger.log_format = LogFormat.from_string(log_format)

            log_to_console = _get_config_bool(config, "logging", "log_to_console")
            if log_to_console is not None:
                self.logger.log_to_console = log_to_console

            log_file_path = _get_config_string(config, "logging", "log_file_path")
            if log_file_path is not None:
                self.logger.log_file_path = log_file_path

            log_response_body = _get_config_bool(config, "logging", "log_response_body")
            if log_response_body is not None:
                self.logger.log_response_body = log_response_body

            log_request_body = _get_config_bool(config, "logging", "log_request_body")
            if log_request_body is not None:
                self.logger.log_request_body = log_request_body

            # general
            host = _get_config_string(config, "general", "host")
            if host is not None:
                self.host = host
                self.base_url = self.host.api_host if isinstance(self.host, PureCloudRegionHosts) else f"https://api.{host}"

        except Exception as e:
            print("[Error] Could not update config:", e)


def _get_config_string(config, section: str, key: str) -> str | None:
    try:
        return str(config[section][key]).strip()
    except:
        return None


def _get_config_bool(config, section: str, key: str) -> bool | None:
    try:
        return config.getboolean(section, key)
    except:
        pass
    return None


def _get_config_int(config, section: str, key: str) -> int | None:
    try:
        return config.getint(section, key)
    except:
        pass
    return None
