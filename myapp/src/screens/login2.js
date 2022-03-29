import {
    Flex,
    Box,
    FormControl,
    FormLabel,
    Input,
    InputGroup,
    HStack,
    InputRightElement,
    Stack,
    Button,
    Heading,
    Text,
    useColorModeValue,
    Link,
    useMediaQuery,
    Center,
  } from '@chakra-ui/react';
  import { ViewIcon, ViewOffIcon } from '@chakra-ui/icons';
  import { useState } from "react";
  import SignInButton from "./LoginWithEmailPassword";
  import GoogleButton from "./SignInWithGoogle";
  
  import {
    Route,
    Redirect
  } from "react-router-dom";
  
  const AuthorizationForm = () => {
    
  
  
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [token, setToken] = useState("");
    const [showPassword, setShowPassword] = useState(false);

    return (
  <Flex  bg={useColorModeValue('gray.50', 'gray.800')} 
        wrap="wrap">
  
              <Stack spacing={8} mx={'auto'} py={12} px={6} flex={0.3}>
                <Stack align={'center'}>
                  <Heading fontSize={'4xl'} textAlign={'center'}>
                    Log In
                  </Heading>
                </Stack>
                
                <Box
                  rounded={'lg'}
                  bg={useColorModeValue('white', 'gray.700')}
                  boxShadow={'lg'}
                  p={8}>
                     
                     <GoogleButton callback={setToken} />
                  <Text align={'center'} fontSize='lg' mt={'1%'} fontWeight='bold'>or</Text>
                  <Stack spacing={4}>
                    <FormControl id="email" isRequired>
                      <FormLabel>Email address</FormLabel>
                      <Input
                          type="email"
                          placeholder="Email"
                          value={email}
                          onChange={(e) => setEmail(e.target.value)}
                      />
                    </FormControl>
                    <FormControl id="password" isRequired>
                      <FormLabel>Password</FormLabel>
                      <InputGroup>
                      <Input
                              type={showPassword ? 'text' : 'password'}
                              placeholder="Password"
                              value={password}
                              onChange={(e) => setPassword(e.target.value)}
                          />
                        <InputRightElement h={'full'}>
                          <Button
                            variant={'ghost'}
                            onClick={() =>
                              setShowPassword((showPassword) => !showPassword)
                            }>
                            {showPassword ? <ViewIcon /> : <ViewOffIcon />}
                          </Button>
                        </InputRightElement>
                      </InputGroup>
                    </FormControl>
                    <Stack spacing={10} pt={2}>
                    <SignInButton
                email={email}
                password={password}
                callback={setToken}
              />
                      
                    </Stack>
                    <Stack pt={6}>
                      <Text align={'center'}  >
                         or <Link  href='/signup' color={'blue.400'}>Create An Account</Link>
                      </Text>
                    </Stack>
                  </Stack>
                </Box>
              </Stack>
              </Flex>
           
    );
  };
  export default AuthorizationForm;
  