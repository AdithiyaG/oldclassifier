import React from "react";
import { ChakraProvider } from "@chakra-ui/react";
import AuthorizationForm from "./screens/Login";
import SignUpForm from "./screens/signup2";
import NotFound from "./screens/ErrorPage";
import Model1 from "./screens/model";
import CallToActionWithIllustration from "./screens/Home";
import Header from "./components/navbar"
import customTheme from "./utils/theme";
import { AuthProvider } from './components/authstate'

import {
  BrowserRouter,
  Routes,
  Route,
  Link 
} from "react-router-dom";


function App() {
  return (
    <ChakraProvider theme={customTheme}>
      <AuthProvider>
      <BrowserRouter>
      <Header />
      <Routes>
      <Route path='/' element={<CallToActionWithIllustration />}/>
      <Route path="login" element={ <AuthorizationForm />}/>
      <Route path="signup" element={ <SignUpForm />}/>
      <Route path="classifier" element={ <Model1 />}/>
      <Route path="*" element={ <NotFound />}/>
      </Routes>
      </BrowserRouter>
      </AuthProvider>
    </ChakraProvider>

    
  );
}

export default App;
