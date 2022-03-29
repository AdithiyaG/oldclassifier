import { Box, Heading, Text, Button,Link } from '@chakra-ui/react';

export default function NotFound() {
  return (
    <Box textAlign="center" py={10} px={6} spacing={20}>
      <Heading
        display="inline-block"
        as="h2"
        size="4xl"
        bgGradient="linear(to-r, primary.100, primary.200)"
        backgroundClip="text">
        404
      </Heading>
      <Text fontSize="18px" mt={3} mb={2}>
        Page Not Found
      </Text>
      <Text color={'gray.500'} mb={6}>
        The page you're looking for does not seem to exist
      </Text>

      <Button
        colorScheme="pink"
        bgGradient="linear(to-r, primary.100, primary.200, primary.300)"
        color="white"
        variant="solid">
            <Link href='/'>
            Go to Home
            </Link>
        
      </Button>
    </Box>
  );
}