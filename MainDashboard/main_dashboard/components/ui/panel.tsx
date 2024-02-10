export default function Panel(props: any) {
  //<Button>{props.activePanel}</Button>;

  return (
    <iframe
      src={props.thisPanel}
      width="100%"
      height="100%"
      allowFullScreen
      className={props.thisPanel != props.activePanel ? "hidden" : ""}
    ></iframe>
  );
}
