function LoadingSpinner() {
  return (
    <div className="flex flex-col items-center justify-center py-12">

      <div className="w-16 h-16 border-4 border-cyan-500 border-t-transparent rounded-full animate-spin"></div>

      <h2 className="text-xl font-semibold text-white mt-6">
        AI is analyzing...
      </h2>

      <p className="text-slate-400 mt-2">
        Please wait a few seconds.
      </p>

    </div>
  );
}

export default LoadingSpinner;