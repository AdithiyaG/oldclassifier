import React from "react";
import { Box, Text,Image,HStack  } from "@chakra-ui/react";

export default function Logo(props) {
  return (
    <Box {...props}>
      <HStack>
      <Image
    boxSize='100px'
    objectFit='cover'
    src='https://bit.ly/dan-abramov'
    alt='Dan Abramov'
  /> 
  <Text fontSize="lg" fontWeight="bold">
        PathoAid
      </Text>
  </HStack>
        
    </Box>
  );
}