import {ReactNode} from "react";
import {createRoot} from "react-dom/client";

export function createIdNode(id: string, node: ReactNode) {
  const element = document.getElementById(id)
  if (element != undefined) {
    createRoot(element).render(node)
  }
}
