<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          Qualificacions App
        </q-toolbar-title>

        <h7 class="text-h6 text-white q-my-md justify-center">{{FechaHoy}} </h7>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header> </q-item-label>
        <EssentialLink v-for="link in essentialLinks" :key="link.title" v-bind="link"/>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
  {
    title: 'Login',
    caption: '',
    icon: 'login',
    to: '/login'
  },
  {
    title: 'About',
    caption: '',
    icon: 'info',
    to: '/about'
  }
]

import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'MainLayout',
  components: {
    EssentialLink
  },

  setup () {
    const leftDrawerOpen = ref(false)
    return {
      essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer () {
        leftDrawerOpen.value = !leftDrawerOpen.value
      }
    }
  },
  computed: {
    FechaHoy () {
      const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
      const dateAct = new Date().toLocaleDateString('ca-Es', options)
      return dateAct.toLocaleUpperCase()
    }
  }
})

</script>
