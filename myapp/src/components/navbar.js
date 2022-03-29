import React from "react";
import {
  Box,
  Stack,
  HStack,
  Heading,
  Flex,
  Text,
  Button,
  useDisclosure,
  Spacer,
  Link,
  Menu,
  MenuButton,
  MenuItem,
  MenuList,
  MenuDivider
} from "@chakra-ui/react";
import { HamburgerIcon,ChevronDownIcon } from "@chakra-ui/icons";

const FeatureMenu=()=>{
  return(  <Menu>
    
  <MenuButton
    variant={'link'}
    cursor={'pointer'}
    minW={0}  >
      <Text fontSize={'lg'}>Features</Text>
  </MenuButton>
  <MenuList bg={'primary.200' } borderColor= "black">
    <MenuItem _hover={{ bg: "primary.100", borderColor: "black" }}> <Link href='/classifier'><Text fontSize={'lg'}>Classifier</Text></Link></MenuItem>
    <MenuDivider />
    <MenuItem _hover={{ bg: "primary.100", borderColor: "black" }}>BSA Calculator</MenuItem>
    <MenuDivider />
    <MenuItem _hover={{ bg: "primary.100", borderColor: "black" }}>Service 3</MenuItem>
  </MenuList>
</Menu>);

}


const Header = (props) => {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const handleToggle = () => (isOpen ? onClose() : onOpen());

  return (
    <Flex
      as="nav"
      align="center"
      justify="space-between"
      wrap="wrap"
      padding={6}
      bg="primary.300"
      color="white"
      {...props}
    >
      <Flex align="center" mr={5}>
        <Link href='/'>
        <Heading as="h1" size="lg" letterSpacing={"widest"}>
          PathoAid
        </Heading>
        </Link>

      </Flex>

      <Box display={{ base: "block", md: "none" }} onClick={handleToggle}>
        <HamburgerIcon />
      </Box>
      <Spacer />
        <Stack  display={{ base: isOpen ? "flex" : "none", md: "flex" }} mx={"auto"} direction={{ base: "column", md: "row" }}        
         width={{ base: "full", md: "auto"  }}
        alignItems="center"
        justify={"space-between"}
        flexGrow={1}
        spacing={'20'}
        >
        <Link   href='/'><Text fontSize={'lg'}>Home</Text></Link>
        
  

        <FeatureMenu />
        <Link href='/'><Text fontSize={'lg'}>Instructions</Text></Link>
        <Link  href='/about'><Text fontSize={'lg'}>About</Text></Link>
        <Link href='/contact'><Text fontSize={'lg'}>Contact</Text></Link>

        <Spacer />
  
        <Stack  display={'flex'}  direction={{ base: "column", md: "row" }} >
        <Button
          variant="ghost"
          _hover={{ bg: "primary.200", borderColor: "black" }}
        >
          <Link href='/signup'>Create account</Link>
        </Button>
        <Button
          variant="ghost"
          _hover={{ bg: "primary.200", borderColor: "black" }}
        >
          <Link href='/login'>LogIn</Link>
        </Button>
       
        </Stack>
    
        </Stack>

        


       
     

   
    </Flex>
  );
};

export default Header;
