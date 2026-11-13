import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import App from "./App";

describe("App", () => {
  it("renders the app title", () => {
    render(<App />);
    const heading = screen.getByRole("heading", { name: "Календарь звонков" });
    expect(heading).toBeDefined();
  });
});
