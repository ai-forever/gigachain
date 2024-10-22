from typing import Union

from pydantic.json_schema import GenerateJsonSchema, JsonSchemaValue, core_schema


class GigaChatJsonSchema(GenerateJsonSchema):
    def field_is_required(
        self,
        field: Union[
            core_schema.ModelField,
            core_schema.DataclassField,
            core_schema.TypedDictField,
        ],
        total: bool,
    ) -> bool:
        """
        Makers nullable fields not required
        """
        if field["schema"]["type"] == "nullable":
            return False
        return super().field_is_required(field, total)

    def nullable_schema(self, schema: core_schema.NullableSchema) -> JsonSchemaValue:
        """
        Remove anyOf if field is nullable
        """
        null_schema = {"type": "null"}
        inner_json_schema = self.generate_inner(schema["schema"])

        if inner_json_schema == null_schema:
            return null_schema
        else:
            return inner_json_schema
