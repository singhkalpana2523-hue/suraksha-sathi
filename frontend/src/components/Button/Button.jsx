function Button({ children, onClick, className = "" }) {

  return (

    <button

      onClick={onClick}

      className={`bg-cyan-500 hover:bg-cyan-600 transition px-8 py-4 rounded-xl font-semibold text-lg ${className}`}

    >

      {children}

    </button>

  );

}

export default Button;