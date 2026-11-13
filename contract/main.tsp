import "@typespec/http";
import "@typespec/openapi";
import "@typespec/openapi3";

using Http;
using OpenAPI;

@service(#{ title: "Calendar API" })
namespace CalendarApi;

/** Response of the health endpoint. */
model Health {
  /** Current service status. */
  status: "ok";
}

/** System endpoints. */
@route("/api")
interface System {
  /** Check that the backend is up. */
  @get
  @route("/health")
  @operationId("getHealth")
  health(): Health;
}
