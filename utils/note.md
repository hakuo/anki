
Code tạo Hint (có khoảng trắng):
```
=IF(OR(EXACT(C1, ""), ISBLANK(C1)), "", IF(ISERR(FIND(" ", C1)),CONCATENATE(LEFT(C1, 1)," ",REGEXREPLACE(MID(C1, 2, LEN(C1)-2),"[a-z]", "_ "),RIGHT(C1, 1)),REGEXREPLACE(REGEXREPLACE(C1,"\b ", "   "), "\B([a-z])", " _")))
```

Code tạo Hint (không có khoảng trắng):
```
=IF(OR(EXACT(C1, ""), ISBLANK(C1)), "", IF(ISERR(FIND(" ", C1)),CONCATENATE(LEFT(C1, 1),REGEXREPLACE(MID(C1, 2, LEN(C1)-2),"[a-z]", "_"),RIGHT(C1, 1)),REGEXREPLACE(REGEXREPLACE(C1,"\b ", "   "), "\B([a-z])", "_")))
```