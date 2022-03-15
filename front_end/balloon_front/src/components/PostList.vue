<template>
  <div>
    <div v-for="(post, key) in Posts" :key="key">
      <hr>
      <p>カテゴリ: {{ post.category }}</p>
      <p>タイトル: {{ post.title }}</p>
      <p>内容: {{ post.content }}</p>
      <p>投稿日: {{ post.published_at}}</p>
      <hr>
    </div>
    <p>this is test</p>
  </div>
</template>


<script>
// import axios from 'axios'
export default {
    name: 'PostList',
    data() {
        return {
            Posts: []
        };
    },
    mounted() {
        this.$axios
            .get("http://localhost:8000/back_end/balloon/posts/")
            .then(response => (this.Posts = response.data))
            .catch(error => console.log(error))
    },
};
</script>