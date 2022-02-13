<template>
  <q-page class="window-height window-width row justify-center items-center">
    <div class="q-pa-md">
      <div class="q-gutter-md" style="max-width: 300px">
        <div class="row">
          <h5 class="text-h5 text-white q-my-md" align="center">Login</h5>
        </div>
        <q-input rounded outlined v-model="nombre" label="Nombre Completo" :rules="[val => !!val || 'Name is missing']"/>
        <q-input rounded outlined v-model="dni" label="DNI" :rules="[val => !!val || 'DNI is missing']"/>
        <q-input rounded outlined v-model="usuario" label="Usuario" :rules="[val => !!val || 'User is missing']"/>
        <q-input rounded outlined v-model="contraseña" label="Contraseña" :rules="[val => !!val || 'Password is missing']"/>
        <q-btn class="btn-fixed-width" rounded color="blue" label="Registrate"/>
        <q-card-section class="text-center q-pa-none">
            <p class="text-grey-6">Ya tienes una cuenta? <a href="http://localhost:8080/#/login">Login</a></p>
          </q-card-section>
      </div>
    </div>
  </q-page>
</template>
<script>
import { ref } from 'vue'
export default {
  setup () {
    return {
      nombre: ref(''),
      dni: ref(''),
      usuario: ref(''),
      contraseña: ref('')
    }
  }
}
</script>

<style lang="sass" scoped>
.btn-fixed-width
  width: 300px
</style>
