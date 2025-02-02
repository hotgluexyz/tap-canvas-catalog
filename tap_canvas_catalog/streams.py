"""Stream type classes for tap-canvas-catalog."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_canvas_catalog.client import CanvasCatalogStream

class UsersStream(CanvasCatalogStream):
    name = "users"
    path = "/users"
    primary_keys = ["id"]
    records_jsonpath = "$.users[*]"
    replication_key = "updated_at"

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
        ),
        th.Property(
            "root_account_id",
            th.IntegerType,
        ),
        th.Property(
            "canvas_user_id",
            th.IntegerType,
        ),
        th.Property(
            "canvas_root_account_uuid",
            th.StringType,
        ),
        th.Property(
            "user_name",
            th.StringType,
        ),
        th.Property(
            "email_address",
            th.StringType,
        ),
        th.Property(
            "custom_fields",
            th.CustomType({"type": ["object", "string"]}),
        ),
        th.Property(
            "created_at",
            th.DateTimeType,
        ),
        th.Property(
            "updated_at",
            th.DateTimeType,
        ),
    ).to_dict()
