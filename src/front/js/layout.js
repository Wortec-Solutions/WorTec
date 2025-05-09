import React, { useState, useEffect } from "react";
import injectContext from "./store/appContext";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";
import { BackendURL } from "./component/backendURL";
import { Navbar } from "./component/navbar";
import { Menu } from "./component/menu";
import { Footer } from "./component/footer";
import { Landing } from "./pages/landing";
import { NotFound } from "./pages/NotFound";

const Layout = () => {
  const basename = process.env.BASENAME || "";

  if (!process.env.BACKEND_URL || process.env.BACKEND_URL === "") 
    return <BackendURL />;

  const [windowWidth, setWindowWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handleResize = () => {
      setWindowWidth(window.innerWidth);
    };

    window.addEventListener("resize", handleResize);
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  return (
    <div className="relative min-h-screen flex flex-col">
      <BrowserRouter basename={basename}>
        <ScrollToTop>
          <Navbar />
          <div className="flex-grow">
            <Routes>
              <Route element={<Landing />} path="/" />
              <Route element={<NotFound />} path="*" />
            </Routes>
          </div>
        </ScrollToTop>
      </BrowserRouter>
    </div>
  );
};


export default injectContext(Layout);

