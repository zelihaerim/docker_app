<h2> <code style="font-size:60px; color: navy; text-indent: 60px; text-transform: uppercase;">Dockerize Streamlit App</code> </h2>
<br>
<code style="color: navy; text-indent: 60px; text-transform: uppercase;">Project Description</code>

<h3>
  <ul>
    <li>  $${\color{blue}  Write \space Poem \space and \space Essay \space app }$$  </li>
    <li> $${\color{blue}  In \space this \space project \space I \space have \space used \space ollama \space gemma2:2b \space model \space and \space Openai \space model.}$$  </li>
    <li> $${\color{blue}  To \space deploy \space streamlit \space and \space FastAPI \space used. }$$ </li>
    <li> $${\color{blue}  To \space run \space program \space write \space terminal\space :\space python \space server.py \space and \space streamlit \space run \space client.py }$$ </li>
  </ul>
</h3>
<h4><code style="color: navy; text-indent: 60px; text-transform: uppercase;">I have used Chat Groq api </code></h4>
<h3>
  <code style="color: navy; text-indent: 60px; text-transform: uppercase;">To run docker images and container: </code>
    <ul>
      <li>  $${\color{magenta}  docker \space build \space -f \space Dockerfile.server \space -t \space server\_image:version1 \space . }$$ </li>
      <li>  $${\color{magenta}  docker \space build \space -f \space Dockerfile.client \space -t \space client\_image:version1 \space . }$$ </li>
      <li>  $${\color{magenta}  docker \space run \space -p \space 8000:8000 \space server\_image:version1 }$$ </li>
      <li>  $${\color{magenta}  docker \space run \space -p \space 8501:8501 \space client\_image:version1 }$$ </li>
    </ul>
</h3>

<h1> $${\color{blue}  Screen \space Shot \space of \space Webapp }$$ </h1>

![1](https://github.com/user-attachments/assets/6227af1a-07d0-42ac-97ae-805495c5c128)
![2](https://github.com/user-attachments/assets/8ca47b78-23bc-4503-b4d2-12c9584c59ff)
![3](https://github.com/user-attachments/assets/e89efbe5-a96b-469c-a7e7-c35136d4d78f)
![4](https://github.com/user-attachments/assets/e9167735-8904-4d1f-9dac-a090ec6df0c8)
