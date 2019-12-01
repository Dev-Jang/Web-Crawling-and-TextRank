# Web-Crawling-and-TextRank (Ver 2.0)

Ver 1.0 에서 Boilerpipe 를 newspaper 모듈로 대체.

두 파일 호환 가능.

<br>
<br>

## run.py

<br>

<b>Function</b>
- To crawl text through Naver search
- Keyword Comparison

<br>

<b>Process</b>
- 검색단어 입력
- 검색건수 출력
- 검색모드 선택
  1. 10 줄 요약
  2. 핵심키워드 비교
- 제목과 내용 출력

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
