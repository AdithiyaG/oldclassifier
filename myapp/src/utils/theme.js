import { extendTheme } from "@chakra-ui/react";

const colors = {
  primary: {
    100: "#CC3350", //mildgreen
    200: "#EA3759",//light green
    300: "#E75B70",// darker than above
    400: "#0EBE6F",//green
    500: "#ff9aa8",
    600: "#0A864F",
    700: "#086F42",
    800: "#075C37",
    900: "#064C2E"
  }
};

const customTheme = extendTheme({ colors });

export default customTheme;