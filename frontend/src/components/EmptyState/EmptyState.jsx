function EmptyState({ message }) {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-12 text-center mt-10">

      <div className="text-6xl mb-5">
        🛡️
      </div>

      <h2 className="text-2xl font-bold text-white">

        No Analysis Yet

      </h2>

      <p className="text-slate-400 mt-4">

        {message}

      </p>

    </div>
  );
}

export default EmptyState;