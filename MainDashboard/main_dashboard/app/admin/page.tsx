"use client";

import Navigation from "@/components/ui/menu";

import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";

export default function Home() {
  return (
    <div className="grid grid-cols-7 grid-rows-8 gap-2 h-screen">
      <div className="bg-black text-white border-white-100">
        <h1>MorePaneeels</h1>
      </div>
      <div className="col-span-6 grid-span-2 bg-black text-white border-white-100">
        <Navigation />
      </div>
      <div className="col-span-7 row-span-7 grid-span-2 bg-black text-white border-white-100">
        <Select>
          <SelectTrigger className="w-[180px]">
            <SelectValue placeholder="Theme" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="light">Light</SelectItem>
            <SelectItem value="dark">Dark</SelectItem>
            <SelectItem value="system">System</SelectItem>
          </SelectContent>
        </Select>
      </div>
    </div>
  );
}
