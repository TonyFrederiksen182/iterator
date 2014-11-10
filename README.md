iterator
========
概要
----
このスクリプトは、第1引数で渡されたファイルの内容を第2引数で渡された数から第3引数で渡された数まで
指定回数反復して標準出力へ書き出すツールです。
この際に、第1引数のファイル中に「${CNT:<format>}」があれば、その時の反復回数の数値が<format>で
指定したようにフォーマットされて置換されます。
※フォーマットはpythonでのフォーマット指定方法と同じです。
　つまり、スクリプト内部でフォーマット指定する文字列を作って、それをpythonインタプリタに流しているだけ。

動機
----
ソフトウェア開発において、「文字列の数値の部分だけ異なるが、その他は同じ内容」（そして、かなり多くの）ファイルを
用意しなければいけない場面があると思います（作者の場合は、割込みベクタを記述するためのアセンブラファイル）。
そのような場合、手作業で1つ1つコピーして、数値の所だけ修正すれば当然できますが、そのコピーする数が多くなればなるほど、
面倒（作者が記述したかった割込みベクタ数は64個でしたが）だったので、作りました。

使い方
------
まず、以下のようなコピー元のテンプレートファイルを用意します。（今回は、template.txt）

＜template.txt＞  
a${CNT:02d}  
b${CNT:03d}  
c${CNT:0.2f}  
  
そして、以下のようにスクリプトを起動します。（さらに標準出力をリダイレクト）  
% python iterator.py template.txt 0 1 > out.txt  

成功した場合、次のような内容のファイルが出来上がります。  
% cat out.txt  
a00  
b000  
c0.00  
  
a01  
b001  
c1.00  


