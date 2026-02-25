package com.kazarella.app

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class KazarellaLinkActivity : AppCompatActivity() {

    private val kazarellaUrl = "https://video-sharing-app-bb0f2.web.app/"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_kazarella_link)

        val openBtn = findViewById<Button>(R.id.btnOpenLink)
        val shareBtn = findViewById<Button>(R.id.btnShareLink)
        val linkText = findViewById<TextView>(R.id.tvLink)

        linkText.text = kazarellaUrl

        openBtn.setOnClickListener {
            openUrl(kazarellaUrl)
        }

        shareBtn.setOnClickListener {
            shareUrl(kazarellaUrl)
        }

        linkText.setOnClickListener {
            openUrl(kazarellaUrl)
        }
    }

    private fun openUrl(url: String) {
        val intent = Intent(Intent.ACTION_VIEW, Uri.parse(url))
        startActivity(intent)
    }

    private fun shareUrl(url: String) {
        val shareIntent = Intent(Intent.ACTION_SEND).apply {
            type = "text/plain"
            putExtra(Intent.EXTRA_TEXT, url)
        }
        startActivity(Intent.createChooser(shareIntent, "شارك رابط كازاريلا"))
    }
}
