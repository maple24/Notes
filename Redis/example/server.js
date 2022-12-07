import express from 'express'
import axios from "axios"
import cors from 'cors'
import Redis from 'redis'

const redisClient = Redis.createClient()
const DEFAULT_EXPIRATION = 3600
const app = express()
app.use(cors())

app.get("/photos", async (req, res) => {
    const albumId = req.query.albumId
    const photos = await getOrSetCache(`photos?albumId=${albumId}`, async () => {
        const { data } = await axios.get("http://photos", { params: { albumId } })
        redisClient.setex(`photos?albumId=${albumId}`, DEFAULT_EXPIRATION, JSON.stringify(data))
        return data
    })
    res.json(photos)
    // redisClient.get(`photos?albumId=${albumId}`, async (error, photos) => {
    //     if (error) console.log(error);
    //     if (photos != null) {
    //         return res.json(JSON.stringify(photos))
    //     } else {
    //         const { data } = await axios.get("http://photo", { params: { albumId } })
    //         redisClient.setex(`photos?albumId=${albumId}`, DEFAULT_EXPIRATION, JSON.stringify(data))
    //         res.json(data)
    //     }
    // })
})

app.get("/photos/:id", async (req, res) => {
    const photo = await getOrSetCache(`photos:${req.params.id}`, async () => {
        const { data } = await axios.get(`http://photos/${req.params.id}`)
        redisClient.setex(`photos:${req.params.id}`, DEFAULT_EXPIRATION, JSON.stringify(data))
        return data
    })
    res.json(photo)
})

function getOrSetCache(key, callback) {
    return new Promise((resolve, rejects) => {
        redisClient.get(key, async (error, data) => {
            if (error) return rejects(error)
            if (data != null) return resolve(JSON.parse(data))  // return here to exit function
            const freshData = await callback()
            redisClient.setex(key, DEFAULT_EXPIRATION, freshData)
            resolve(freshData)
        })
    })
}

app.listen(3000)