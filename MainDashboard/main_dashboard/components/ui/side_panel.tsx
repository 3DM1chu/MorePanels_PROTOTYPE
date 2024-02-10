"use client";

import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area";
import { useState, useEffect } from "react";
import { Badge } from "@/components/ui/badge";

export default function SidePanel(props: any) {
  const [panels, setPanels] = useState<any[]>([]);
  const setActivePanel = props.changePanel;

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("http://127.0.0.1:8009/panels");
      const data = await response.json();
      console.log(data["panels"]);
      setPanels(data["panels"]);
    };

    fetchData();
  }, []);

  return (
    <div>
      <ScrollArea className="w-100 h-96 whitespace-nowrap rounded-md border">
        <Accordion type="single" collapsible>
          {panels.map((panel) => (
            <AccordionItem value={panel["name"]} key={panel["name"]}>
              <AccordionTrigger>{panel["name"]}</AccordionTrigger>
              <AccordionContent className="flex flex-row content-center items-center">
                <Badge
                  className="text-white h-10"
                  variant="outline"
                  onClick={() => setActivePanel(panel["url"])}
                >
                  WEJDŹ
                </Badge>
              </AccordionContent>
            </AccordionItem>
          ))}
        </Accordion>
        <ScrollBar orientation="vertical" />
      </ScrollArea>
    </div>
  );
}
