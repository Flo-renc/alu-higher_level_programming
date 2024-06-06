#!/usr/bin/node
// check the number of argumrnts
if (process.argv.length < 3) {
  console.log('No argument');
} else {
  // Extract the first argument (index 2 in process.argv)
  const firstArgument = process.argv[2];
  console.log(firstArgument);
}
