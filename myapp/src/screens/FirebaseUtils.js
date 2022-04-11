import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// const firebaseConfig = {
//   apiKey: "__YOUR_API_KEY__",
//   authDomain: "__YOUR_AUTH_DOMAIN__",
//   projectId: "__Your_PROJECT_ID__",
//   storageBucket: "__BUCKET__",
//   messagingSenderId: "___sender_id__",
//   appId: "__appid__",
//   measurementId: "optional",
// };
const firebaseConfig = {
  apiKey: "AIzaSyApfBiErHTG_raSUWlleK57sVeiMMNY1iM",
  authDomain: "breastcancermodel.firebaseapp.com",
  projectId: "breastcancermodel",
  storageBucket: "breastcancermodel.appspot.com",
  messagingSenderId: "892641583634",
  appId: "1:892641583634:web:ec68a3b6b9b0ca281d2ecb"
};
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);


