import { Button,Text,Center } from "@chakra-ui/react";
import { GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import { auth } from "./FirebaseUtils";
import { FcGoogle } from 'react-icons/fc';

const GoogleButton = ({ callback }) => {
 
  const onClick = async () => {
    const res = await signInWithPopup(auth, new GoogleAuthProvider());
    console.log(res.credential.idToken)
    const user = res.user;
    console.log(user);
    let idToken = await user.getIdToken(true);
    callback(idToken);
    // Verify and register user with backend
    const response = await fetch("http://localhost:8000/api1/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `JWT ${idToken}`,
      },
    });
    const data = await response.json();
    console.log(data);
  };

  return <Button onClick={onClick}  w={'full'} maxW={'md'} variant={'outline'} leftIcon={<FcGoogle />}><Center><Text>Sign in with Google</Text> </Center></Button>;
};

export default GoogleButton;
