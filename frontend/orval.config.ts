import { defineConfig } from "orval";

export default defineConfig({
  calendar: {
    input: "../contract/out/openapi.yaml",
    output: {
      target: "./src/shared/api/generated.ts",
      client: "fetch",
      mode: "single",
      clean: true,
      baseUrl: "http://127.0.0.1:8000",
    },
  },
});
