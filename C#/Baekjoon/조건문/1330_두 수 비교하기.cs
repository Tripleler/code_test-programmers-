﻿//https://www.acmicpc.net/problem/1330
string[] s = Console.ReadLine().Split();
int a = int.Parse(s[0]);
int b = int.Parse(s[1]);
Console.WriteLine((a > b) ? ">" : (a < b) ? "<" : "==");