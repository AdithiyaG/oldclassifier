import {
    Button,
    Center,
    Container,
    FormControl,
    FormLabel,
    Heading,
    HStack,
    Input,
    VStack,
    Text,
    Box,
  } from "@chakra-ui/react";

  const Results=()=>{
    return(
<Box>
<Text fontSize='3xl'>Result</Text>
  <HStack>
  
  <Text>
  Class:
  </Text>
  <Text>
  Benign
  </Text>
  </HStack>
    
  <HStack>
  <Text>
  Accuracy:
  </Text>
  <Text>
  97%
  </Text>
  </HStack>
  <HStack>
  <Text>
  Description:
  </Text>
  <Text>
  Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
  molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
  numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
  optio, eaque rerum! 
  </Text>
  </HStack>
  <Text align={'center'} >Want to know more about Benign?</Text>
  
  </Box>
    );
    
  }

  export default Results;