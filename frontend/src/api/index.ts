const API_URL = '/api/'
export type Emotion = {
  angry: number
  disgust: number
  fear: number
  happy: number
  sad: number
  surprise: number
  neutral: number
}
export type MeetingKey = {
  key: string
}
export const uploadImageToAPI = async (imageBase64: string) => {
  const url = API_URL + 'emotion_estimate'
  const payload = {
    img: imageBase64
  }

  return await fetch(url, {
    mode: 'cors',
    method: 'POST',
    body: JSON.stringify(payload),
    headers: {
      'content-type': 'application/json'
    }
  })
    .then(response => {
      return response.json() as Promise<Emotion>
    })
    .catch(err => {
      throw err
    })
}
export const CreateMeeting = async () => {
  const url = API_URL + 'meeting'

  return await fetch(url, {
    mode: 'cors',
    method: 'POST',
    headers: {
      'content-type': 'application/json'
    }
  })
    .then(response => {
      return response.json() as Promise<MeetingKey>
    })
    .catch(err => {
      throw err
    })
}
export const JoinMeeting = async (meeting_key: string) => {
  const url = API_URL + 'meeting/join'
  const payload = {
    key: meeting_key
  }

  return await fetch(url, {
    mode: 'cors',
    method: 'POST',
    body: JSON.stringify(payload),
    headers: {
      'content-type': 'application/json'
    }
  })
    .then(response => {
      return response.json() as Promise<MeetingKey>
    })
    .catch(err => {
      throw err
    })
}
