export const uploadImageToAPI = async (imageBase64: string) => {
  const API_URL = '/api/emotion_estimate'
  const payload = {
    img: imageBase64
  }

  await fetch(API_URL, {
    mode: 'cors',
    method: 'POST',
    body: JSON.stringify(payload)
  })
    .then(response => {
      return response.json()
    })
    .catch(err => {
      return { message: err }
    })
}
