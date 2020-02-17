from indy_common.authorize.auth_request_validator import WriteRequestValidator

from indy_common.constants import SET_RICH_SCHEMA_MAPPING

from indy_node.server.request_handlers.domain_req_handlers.rich_schema.abstract_rich_schema_object_handler import \
    AbstractRichSchemaObjectHandler

from plenum.server.database_manager import DatabaseManager
from stp_core.common.log import getlogger

logger = getlogger()


class RichSchemaMappingHandler(AbstractRichSchemaObjectHandler):

    def __init__(self, database_manager: DatabaseManager,
                 write_req_validator: WriteRequestValidator):
        super().__init__(SET_RICH_SCHEMA_MAPPING, database_manager, write_req_validator)
