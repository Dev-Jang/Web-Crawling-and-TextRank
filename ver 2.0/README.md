# Web-Crawling-and-TextRank (Ver 2.0)

Replaced BoilerPipe with the Newspaper module.

Both files are compatible and run successfully.

<br>
<br>

## run.py

<br>

<b>Function</b>
- To crawl text through Naver search
- Key Keyword Comparison Output

<br>

<b>Process</b>
- Enter search word
- Search count output
- Select search mode
  1. 10 line summary
  2. Keyword Comparison
- Print title and content

<pre><code><b>Execution result</b>

> 검색단어 : [입력]
검색된 결과 <건수> 건
> 검색번호(1-1000) : [입력]
***************************
모드를 선택해주세요.
1. 10 Line Summarize
2. Keyword Comparison
> 입력(숫자만) : [입력]
***************************
- 제목 : <포스트 제목>
- 내용
<포스트 내용(텍스트)>
</code></pre>

<br>
<br>

## TextRank.py

<br>

<b>Function</b>
- Summarize documents using the TextRank algorithm
- Output key words by weighting each word

<br>

<b>Process</b>
- Crawl Text
- Sentence division
- Natural language processing(NLP)
- TF-IDF Model
- Generate graph
- Apply TextRank

<br>
<br>

## Reference
https://excelsior-cjh.tistory.com/93
