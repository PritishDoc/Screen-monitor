const ScreenshotGrid = ({ screenshots }) => (
  <div className="grid grid-cols-3 gap-4">
    {screenshots.map((src, i) => (
      <img key={i} src={src} alt={`screenshot-${i}`} className="rounded" />
    ))}
  </div>
);
