<template>
  <v-container class="text-xs-center">
    <v-card flat>
      <v-card-title primary-title>
        <h4>Вход</h4>
      </v-card-title>
      <v-form>
        <v-text-field
          v-model="username"
          prepend-icon="person"
          label="Имя пользователя">
        </v-text-field>
        <v-text-field
          v-model="password"
          prepend-icon="lock"
          label="Пароль"
          type="password">
        </v-text-field>
        <v-card-actions>
          <v-btn @click="submitForm" block>Войти</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "LogIn",
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    submitForm() {
      const formData = {"username": this.username, "password": this.password}
      this.axios.defaults.headers.common["Authorization"] = ""
      localStorage.removeItem("token")

      this.axios
        .post("/api/token/login", formData)
        .then(responce => {
          const token = responce.data.auth_token

          this.$store.commit("SET_TOKEN", token)
          this.axios.defaults.headers.common["Authorization"] = "Token " + token
          localStorage.setItem("token", token)

          const toPath = this.$route.query.to || "/"
          this.$router.push(toPath)
        })
        .catch(errors => {})
    }
  },
  mounted() {
    document.title = "Log In | TR"
  }
};
</script>

<style scoped>
</style>