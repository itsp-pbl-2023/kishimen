export type Emotion = {
  angry: number
  disgust: number
  fear: number
  happy: number
  sad: number
  surprise: number
  neutral: number
}
export const uploadImageToAPI = async (imageBase64: string) => {
  const API_URL = '/api/emotion_estimate'
  const payload = {
    img: imageBase64
  }

  return await fetch(API_URL, {
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
