import { useRef } from "react";

function UploadArea({
  file,
  setFile,
  accept,
  title,
  subtitle,
}) {
  const inputRef = useRef(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];

    if (selectedFile) {
      setFile(selectedFile);
    }
  };

  return (
    <div>
      <div
        onClick={() => inputRef.current.click()}
        className="border-2 border-dashed border-cyan-500 rounded-2xl p-12 text-center cursor-pointer hover:bg-slate-900 transition"
      >
        <h2 className="text-2xl font-semibold text-white">
          {title}
        </h2>

        <p className="text-slate-400 mt-3">
          {subtitle}
        </p>

        <input
          ref={inputRef}
          type="file"
          accept={accept}
          className="hidden"
          onChange={handleFileChange}
        />
      </div>

      {file && (
        <div className="mt-5 bg-slate-900 p-4 rounded-xl border border-slate-800">
          <p className="text-cyan-400 font-semibold">
            Selected File
          </p>

          <p className="text-slate-300 mt-2">
            {file.name}
          </p>
        </div>
      )}
    </div>
  );
}

export default UploadArea;