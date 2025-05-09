import React, { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import wortecLogo from "/workspaces/WorTec/src/front/img/wortec-only-logo.jpeg";
import wortecMovil from "/workspaces/WorTec/src/front/img/wortec-logo.png";

export const Navbar = () => {
  const location = useLocation();
  const [windowWidth, setWindowWidth] = useState(window.innerWidth);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    const handleResize = () => setWindowWidth(window.innerWidth);
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  const isMobile = windowWidth <= 690;

  return (
    <nav className="fixed top-0 w-full bg-transparent text-white z-50">
      {isMobile ? (
        <nav className="fixed top-0 w-full bg-black text-white z-50 shadow-md">
          {/* Encabezado con logo y hamburguesa */}
          <div className="flex items-center justify-between px-4 py-3">
            {/* Logo */}
            <a href="#" className="flex items-center">
              <img src={wortecMovil} alt="WorTec Logo" className="h-10" />
            </a>

            {/* Menú hamburguesa con swap de icono */}
            <label className="btn btn-circle swap swap-rotate">
              {/* Este checkbox oculto controla el estado */}
              <input
                type="checkbox"
                checked={menuOpen}
                onChange={() => setMenuOpen(!menuOpen)}
                className="hidden"
              />

              {/* Icono hamburguesa */}
              <svg
                className={`swap-off fill-current transition-transform duration-300 ${menuOpen ? "hidden" : ""}`}
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                viewBox="0 0 512 512"
              >
                <path d="M64,384H448V341.33H64Zm0-106.67H448V234.67H64ZM64,128v42.67H448V128Z" />
              </svg>

              {/* Icono de cierre */}
              <svg
                className={`swap-on fill-current transition-transform duration-300 ${menuOpen ? "" : "hidden"}`}
                xmlns="http://www.w3.org/2000/svg"
                width="32"
                height="32"
                viewBox="0 0 512 512"
              >
                <polygon points="400 145.49 366.51 112 256 222.51 145.49 112 112 145.49 222.51 256 112 366.51 145.49 400 256 289.49 366.51 400 400 366.51 289.49 256 400 145.49" />
              </svg>
            </label>
          </div>

          {/* Menú desplegable */}
          {menuOpen && (
            <div className="bg-black text-white flex flex-col items-center justify-center space-y-6 py-8">
              {["Inicio", "Nosotros", "Servicios", "Contacto", "Blog"].map(
                (item) => (
                  <a
                    key={item}
                    href="#"
                    className="text-lg font-medium relative after:absolute after:bottom-0 after:left-0 after:w-full after:h-[2px] after:bg-orange-600 after:scale-x-0 hover:after:scale-x-100 after:transition-transform after:duration-300"
                  >
                    {item}
                  </a>
                )
              )}
            </div>
          )}
        </nav>
      ) : (
        <div
          className="relative bg-black 
        shadow-[inset_4px_4px_8px_rgba(255,255,255,0.15),inset_-4px_-4px_8px_rgba(0,0,0,0.7),0_15px_30px_rgba(0,0,0,0.8)]
        text-white max-w-6xl w-full mx-auto mt-5 rounded-full py-4 px-10 mb-5 border border-[#222222] overflow-hidden"
        >
          <div className="absolute top-0 left-0 w-full h-2/3 rounded-full bg-white/25 blur-lg pointer-events-none"></div>

          <div className="flex items-center justify-b w-full">
            {/* Logo alineado a la izquierda */}
            <div className="flex items-center flex-[1.5]">
              <a href="#" className="flex items-center">
                <img src={wortecLogo} alt="WorTec Logo" className="h-14 mr-3" />
                <span className="self-center text-lg font-semibold whitespace-nowrap text-white">
                  WORTEC
                </span>
              </a>
            </div>

            {/* Menú centrado */}
            <div className="flex justify-center flex-[3]">
              <ul className="flex space-x-10 text-lg font-medium text-white">
                <li>
                  <a
                    href="#"
                    className="relative transition-all duration-300 after:absolute after:bottom-0 after:left-0 after:w-full after:h-[6px] after:bg-orange-600 after:scale-x-0 hover:after:scale-x-100 after:transition-all after:duration-300 "
                  >
                    Inicio
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="relative transition-all duration-300 after:absolute after:bottom-0 after:left-0 after:w-full after:h-[6px] after:bg-orange-600 after:scale-x-0 hover:after:scale-x-100 after:transition-all after:duration-300"
                  >
                    Nosotros
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="relative transition-all duration-300 after:absolute after:bottom-0 after:left-0 after:w-full after:h-[6px] after:bg-orange-600 after:scale-x-0 hover:after:scale-x-100 after:transition-all after:duration-300"
                  >
                    Servicios
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="relative transition-all duration-300 after:absolute after:bottom-0 after:left-0 after:w-full after:h-[6px] after:bg-orange-600 after:scale-x-0 hover:after:scale-x-100 after:transition-all after:duration-300"
                  >
                    Contacto
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="relative  transition-all duration-300 after:absolute after:bottom-0 after:left-0 after:w-full after:h-[6px] after:bg-orange-600 after:scale-x-0 hover:after:scale-x-100 after:transition-all after:duration-300"
                  >
                    Blog
                  </a>
                </li>
              </ul>
            </div>

            {/* Botón a la derecha */}
            <div className="relative flex items-center justify-end flex-[1.5]">
              <button
                className="bg-orange-400 text-white text-lg font-bold rounded-full px-6 py-2 
               shadow-md shadow-orange-500/50 hover:shadow-xl hover:shadow-orange-600/40 
               transition-all duration-300 focus:outline-none border-4 border-orange-500
               transform hover:scale-105 active:scale-95 active:translate-y-1"
              >
                Agendá tu cotización
              </button>
            </div>
          </div>
        </div>
      )}
    </nav>
  );
};
