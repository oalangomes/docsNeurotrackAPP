# Modelos de Dados do NeuroTrack - Extraídos do Swagger

## Modelos Principais

### User
```json
{
  "type": "object",
  "properties": {
    "_id": {"type": "string"},
    "name": {"type": "string"},
    "email": {"type": "string"},
    "password": {"type": "string"}
  },
  "required": ["name", "email", "password"]
}
```

### UserRegistration
```json
{
  "type": "object",
  "properties": {
    "auth": {
      "type": "object",
      "properties": {
        "local": {
          "type": "object",
          "properties": {
            "email": {"type": "string"},
            "password": {"type": "string"}
          },
          "required": ["email", "password"]
        }
      }
    },
    "profile": {
      "type": "object",
      "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
      },
      "required": ["name", "age"]
    },
    "neuroProfile": {
      "type": "object",
      "properties": {
        "type": {"type": "string"},
        "diagnoses": {
          "type": "array",
          "items": {"type": "string"}
        },
        "symptoms": {
          "type": "array",
          "items": {"type": "string"}
        },
        "medicationSchedule": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {"type": "string"},
              "dosage": {"type": "string"},
              "times": {
                "type": "array",
                "items": {"type": "string"}
              }
            }
          }
        }
      }
    },
    "preferences": {"type": "object"},
    "system": {
      "type": "object",
      "properties": {
        "lang": {"type": "string", "example": "pt"}
      }
    }
  }
}
```

### Task
```json
{
  "type": "object",
  "properties": {
    "title": {"type": "string"},
    "description": {"type": "string"},
    "completed": {"type": "boolean"}
  },
  "required": ["title"]
}
```

### DailyEntry
```json
{
  "type": "object",
  "properties": {
    "text": {"type": "number"},
    "note": {"type": "string"},
    "date": {"type": "string", "format": "date"}
  },
  "required": ["mood", "date"]
}
```

### ErrorResponse
```json
{
  "type": "object",
  "properties": {
    "success": {"type": "boolean", "example": false},
    "error": {
      "type": "object",
      "properties": {
        "message": {"type": "string"},
        "code": {"type": "string"}
      }
    }
  }
}
```

## Exemplos de Requisições e Respostas

### Registro de Usuário
```json
{
  "auth": {
    "local": {
      "email": "john.doe@example.com",
      "password": "password123"
    }
  },
  "profile": {
    "name": "John Doe",
    "age": 30
  },
  "neuroProfile": {
    "type": "Neurodivergent",
    "diagnoses": ["ADHD", "ASD"],
    "symptoms": ["Difficulty focusing", "Sensory sensitivity"],
    "medicationSchedule": [
      {
        "name": "Medication A",
        "dosage": "10mg",
        "times": ["08:00", "20:00"]
      }
    ]
  },
  "preferences": {
    "type": "NeuroPreferencesSchema"
  },
  "system": {
    "lang": "en"
  }
}
```

### Entrada Diária
```json
{
  "text": "This is my daily entry.",
  "date": "2025-03-25",
  "mood": 4
}
```

### Tarefa
```json
{
  "title": "New Task",
  "description": "This is a new task.",
  "dueDate": "2025-03-30",
  "priority": 3,
  "sensoryTags": ["urgent", "creative"],
  "assignedTo": ["userId1", "userId2"]
}
```

### Evento de Calendário
```json
{
  "title": "Consulta médica",
  "date": "2025-04-15",
  "time": "14:30",
  "location": "Clínica Central"
}
```

### Preferências de Usuário
```json
{
  "style": "motivacional",
  "lang": "pt",
  "themes": ["foco", "relaxamento"]
}
```

### Perfil Neurodivergente
```json
{
  "type": "Neurodivergente",
  "diagnoses": ["TDAH", "TEA"],
  "symptoms": ["Hiperfoco", "Distração"],
  "medicationSchedule": [
    {
      "name": "Medicação A",
      "dosage": "10mg",
      "times": ["08:00", "20:00"]
    }
  ]
}
```
