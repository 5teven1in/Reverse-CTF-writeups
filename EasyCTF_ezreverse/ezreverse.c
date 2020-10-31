#include "defs.h"
#include <stdio.h>

int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax
  int v4; // [rsp+10h] [rbp-20h]
  int v5; // [rsp+14h] [rbp-1Ch]
  __int64 v6; // [rsp+18h] [rbp-18h]
  int v7; // [rsp+20h] [rbp-10h]
  char *v8; // [rsp+28h] [rbp-8h]

  // signal(2, sigintHandler);
  // target = (char *)*argv;
  // if ( argc != 2 )
  //   return 2;
  char input[10];
  klee_make_symbolic(input, sizeof(input), "input");
  // v8 = argv[1];
  v8 = input;
  v4 = 1;
  v5 = 2;
  v6 = 0x400000003LL;
  v7 = 5;
  v4 = *v8 + 1;
  v5 = v8[1] + 2;
  LODWORD(v6) = v8[2] + 3;
  HIDWORD(v6) = v8[3] + 4;
  v7 = v8[4] + 5;
  if ( v6 != 0x6F0000007DLL || v4 != v7 - 10 || v5 != 53 || v7 != HIDWORD(v6) + 3 )
  {
    // sleep(2u);
    // remove(*argv);
    puts("successfully deleted!");
    result = 2;
  }
  else
  {
    klee_assert(0);
    printf("Now here is your flag: ");
    // print_5(&v4);
    result = 1;
  }
  return result;
}
