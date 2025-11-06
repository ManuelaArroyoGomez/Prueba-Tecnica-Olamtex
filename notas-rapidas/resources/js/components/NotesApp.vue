<template>
  <div class="min-h-screen bg-slate-50 py-10">
    <div class="mx-auto w-full max-w-2xl px-4">

      <!-- Header -->
      <div class="mb-6">
        <h1
          class="text-4xl font-extrabold tracking-tight bg-gradient-to-r from-indigo-700 via-fuchsia-600 to-rose-500 bg-clip-text text-transparent"
        >
          Notas Rápidas
        </h1>
      </div>

      <!-- Card: formulario -->
      <div class="rounded-2xl bg-white shadow-sm ring-1 ring-slate-200 p-5 mb-8">
        <form @submit.prevent="addNote" class="space-y-3">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Título</label>
            <input
              v-model="title"
              class="w-full rounded-xl border-slate-300 bg-white px-3 py-2 text-slate-900 shadow-sm
                     focus:border-indigo-500 focus:ring-4 focus:ring-indigo-200 transition"
              placeholder="Ej. Compras, Ideas, Tareas…"
            />
            <p v-if="errors.title" class="mt-1 text-xs text-rose-600">{{ errors.title[0] }}</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Contenido</label>
            <textarea
              v-model="content"
              rows="4"
              class="w-full rounded-xl border-slate-300 bg-white px-3 py-2 text-slate-900 shadow-sm
                     focus:border-indigo-500 focus:ring-4 focus:ring-indigo-200 transition"
              placeholder="Escribe tu nota…"
            />
            <p v-if="errors.content" class="mt-1 text-xs text-rose-600">{{ errors.content[0] }}</p>
          </div>

          <div class="flex items-center justify-end gap-2 pt-1">
            <button
              class="inline-flex items-center gap-2 rounded-xl bg-indigo-600 px-4 py-2 font-medium text-white
                     shadow-sm hover:bg-indigo-700 active:bg-indigo-800 disabled:opacity-60 transition"
              :disabled="!title.trim() || !content.trim()"
            >
              Guardar
            </button>
          </div>
        </form>
      </div>

      <!-- Estados -->
      <div v-if="loading" class="text-slate-500">Cargando…</div>
      <div v-else-if="fail" class="text-rose-600">{{ fail }}</div>
      <div v-else-if="!notes.length" class="text-slate-500">
        Aún no hay notas
      </div>

      <!-- Grid/List de notas -->
      <ul v-else class="space-y-4">
        <li
          v-for="n in notes"
          :key="n.id"
          class="rounded-2xl bg-white p-5 shadow-sm ring-1 ring-slate-200 transition hover:shadow-md"
        >
          <!-- Vista normal -->
          <div v-if="editing?.id !== n.id">
            <div class="flex items-start gap-3">
              <div class="flex-1">
                <h3 class="text-lg font-semibold text-slate-900">{{ n.title }}</h3>
                <p class="mt-1 text-slate-700 whitespace-pre-line">{{ n.content }}</p>
              </div>
              <div class="flex gap-2">
                <button
                  class="rounded-lg px-3 py-1.5 text-sm font-medium text-indigo-700 bg-indigo-50 hover:bg-indigo-100 transition"
                  @click="startEdit(n)"
                >
                  Editar
                </button>
                <button
                  class="rounded-lg px-3 py-1.5 text-sm font-medium text-rose-700 bg-rose-50 hover:bg-rose-100 transition"
                  @click="remove(n.id)"
                >
                  Eliminar
                </button>
              </div>
            </div>
          </div>

          <!-- Modo edición -->
          <div v-else class="space-y-3">
            <input
              v-model="editing.title"
              class="w-full rounded-xl border-slate-300 px-3 py-2 focus:border-indigo-500 focus:ring-4 focus:ring-indigo-200 transition"
            />
            <textarea
              v-model="editing.content"
              rows="3"
              class="w-full rounded-xl border-slate-300 px-3 py-2 focus:border-indigo-500 focus:ring-4 focus:ring-indigo-200 transition"
            />
            <div class="flex gap-2">
              <button
                class="rounded-lg bg-emerald-600 px-3 py-1.5 text-sm font-medium text-white hover:bg-emerald-700 transition"
                @click="saveEdit"
              >
                Guardar
              </button>
              <button
                class="rounded-lg bg-slate-100 px-3 py-1.5 text-sm font-medium text-slate-700 hover:bg-slate-200 transition"
                @click="cancelEdit"
              >
                Cancelar
              </button>
            </div>
            <p v-if="editErrors.title" class="text-xs text-rose-600">{{ editErrors.title[0] }}</p>
            <p v-if="editErrors.content" class="text-xs text-rose-600">{{ editErrors.content[0] }}</p>
          </div>
        </li>
      </ul>

      <!-- Footer mini -->
      <p class="mt-10 text-center text-xs text-slate-400">
        Hecho por Manuela Arroyo 💜
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

type Note = { id:number; title:string; content:string; created_at?:string; updated_at?:string }

// estado principal
const notes   = ref<Note[]>([])
const title   = ref('')
const content = ref('')

// estados de UI
const loading = ref(false)
const fail    = ref<string | null>(null)
const errors  = ref<{ title?: string[]; content?: string[] }>({})

// edición
const editing     = ref<{ id:number; title:string; content:string } | null>(null)
const editErrors  = ref<{ title?: string[]; content?: string[] }>({})

const getNotes = async () => {
  loading.value = true
  fail.value = null
  try {
    const { data } = await axios.get('/api/notes')
    notes.value = data
  } catch {
    fail.value = 'No se pudieron cargar las notas.'
  } finally {
    loading.value = false
  }
}

const addNote = async () => {
  errors.value = {}
  try {
    const { data } = await axios.post('/api/notes', {
      title: title.value.trim(),
      content: content.value.trim(),
    })
    notes.value.unshift(data)  // aparece arriba
    title.value = ''
    content.value = ''
  } catch (e:any) {
    if (e.response?.status === 422) errors.value = e.response.data.errors
  }
}

const startEdit = (n: Note) => {
  editing.value = { id: n.id, title: n.title, content: n.content }
  editErrors.value = {}
}

const cancelEdit = () => {
  editing.value = null
  editErrors.value = {}
}

const saveEdit = async () => {
  if (!editing.value) return
  editErrors.value = {}
  try {
    const { data } = await axios.put(`/api/notes/${editing.value.id}`, {
      title: editing.value.title.trim(),
      content: editing.value.content.trim(),
    })
    const i = notes.value.findIndex(x => x.id === data.id)
    if (i > -1) notes.value[i] = data
    editing.value = null
  } catch (e:any) {
    if (e.response?.status === 422) editErrors.value = e.response.data.errors
  }
}

const remove = async (id:number) => {
  await axios.delete(`/api/notes/${id}`)
  notes.value = notes.value.filter(n => n.id !== id)
}

onMounted(getNotes)
</script>
