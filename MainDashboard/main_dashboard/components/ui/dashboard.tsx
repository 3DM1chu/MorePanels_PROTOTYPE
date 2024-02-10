"use client";

import SidePanel from "@/components/ui/side_panel";
import { useState } from "react";
import Panel from "./panel";
import Navigation from "./menu";

var panels = Array();

export default function Dashboard() {
  const [activePanel, setActivePanel] = useState<string>("");

  const changeActivePanel = (arg: string) => {
    setActivePanel(arg);
    if (!panels.includes(arg)) {
      panels.push(arg);
    }
  };

  return (
    <div className="grid grid-cols-7 grid-rows-8 gap-2 h-screen">
      <div className="bg-black text-white border-white-100">
        <h1>MorePaneeels</h1>
      </div>
      <div className="col-span-6 grid-span-2 bg-black text-white border-white-100">
        <Navigation />
      </div>
      <div className="bg-black row-span-7 text-white border-white-100">
        <SidePanel changePanel={changeActivePanel} />
      </div>
      <div className="col-span-6 row-span-7 grid-span-2 bg-black text-white border-white-100">
        {panels.map((panel) => (
          <Panel thisPanel={panel} activePanel={activePanel} />
        ))}
      </div>
    </div>
  );
}
