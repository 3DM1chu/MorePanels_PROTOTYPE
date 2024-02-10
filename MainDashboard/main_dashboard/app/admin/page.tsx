"use client";

import Navigation from "@/components/ui/menu";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";

import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";

export default function Home() {
  const formSchema = z.object({
    name: z.string().min(2).max(50),
    url: z.string().url(),
  });

  // 1. Define your form.
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      name: "",
      url: "",
    },
  });

  // 2. Define a submit handler.
  function onSubmit(values: z.infer<typeof formSchema>) {
    // Do something with the form values.
    // ✅ This will be type-safe and validated.
    console.log(values);
    fetch("http://localhost:8009/panel", {
      method: "POST",
      body: JSON.stringify(values),
      headers: {
        "Content-Type": "application/json",
      },
    });
    form.reset();
    toast("Panel added", {
      description: "Panel " + values.name + " is available in main dashboard",
      action: {
        label: "Undo",
        onClick: () => {
          fetch("http://localhost:8009/panel", {
            method: "DELETE",
            body: JSON.stringify(values),
            headers: {
              "Content-Type": "application/json",
            },
          })
            .then((resp) => resp.text())
            .then((resp) => console.log(resp));
        },
      },
    });
  }

  return (
    <div className="grid grid-cols-7 grid-rows-8 gap-2 h-screen">
      <div className="bg-black text-white border-white-100">
        <h1>MorePaneeels</h1>
      </div>
      <div className="col-span-6 grid-span-2 bg-black text-white border-white-100">
        <Navigation />
      </div>
      <div className="col-span-7 row-span-7 grid-span-2 bg-black text-white border-white-100">
        <div className="grid justify-items-center my-16">
          <Form {...form}>
            <form
              onSubmit={form.handleSubmit(onSubmit)}
              className="w-80 space-y-8"
            >
              <FormField
                control={form.control}
                name="name"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Name of panel</FormLabel>
                    <FormControl>
                      <Input placeholder="PANEL_0" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="url"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>URL of panel</FormLabel>
                    <FormControl>
                      <Input placeholder="http://localhost:3000" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <Button type="submit">Submit</Button>
            </form>
          </Form>
        </div>
      </div>
    </div>
  );
}
