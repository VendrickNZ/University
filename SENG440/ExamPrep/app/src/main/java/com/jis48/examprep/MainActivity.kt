package com.jis48.examprep

import android.annotation.SuppressLint
import android.graphics.Paint.Align
import android.graphics.drawable.shapes.Shape
import android.os.Bundle
import android.widget.Button
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonColors
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextField
import androidx.compose.material3.TextFieldDefaults
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.RectangleShape
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.jis48.examprep.ui.theme.DarkGreen
import com.jis48.examprep.ui.theme.ExamPrepTheme


class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)
        setContent {
            ExamPrepTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    MainScreen()
                }
            }
        }
    }
}

@SuppressLint("UnusedMaterial3ScaffoldPaddingParameter")
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun MainScreen() {
    Scaffold(
        topBar = {
            TopAppBar(title = { Text("Sort of Game")},
                colors = TopAppBarDefaults.smallTopAppBarColors(containerColor = DarkGreen, titleContentColor = Color.White))
        }
    ) {
        Column (modifier = Modifier.padding(it)){
            Spacer(Modifier.weight(0.3f))  // This will push the buttons to the bottom
            InputFields(/* parameters */)
            Spacer(Modifier.weight(1f))  // This will push the buttons to the bottom
            LargeTextBox(/* parameters */)
            Spacer(Modifier.weight(1f))  // This will push the buttons to the bottom
            ActionButtons(/* parameters */)
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun InputFields() {
    val fromText = rememberSaveable { mutableStateOf("")}
    val toText = rememberSaveable { mutableStateOf("")}
    Column (modifier = Modifier.padding(16.dp)) {
        Row (modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.Center,
            verticalAlignment = Alignment.CenterVertically) {
            Text("From", color = Color.Gray, textAlign = TextAlign.Left)
            Spacer(Modifier.width(16.dp))
            OutlinedTextField(value = fromText.value, onValueChange = {newText ->
                fromText.value = newText
            })
        }

        Row (modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.Center,
            verticalAlignment = Alignment.CenterVertically) {
            Text("To", color = Color.Gray)
            Spacer(Modifier.width(16.dp))
            OutlinedTextField(value = toText.value, onValueChange = {newText ->
                toText.value = newText
            })
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LargeTextBox() {
    val textBoxText = rememberSaveable { mutableStateOf("")}
    Box (modifier = Modifier
        .fillMaxWidth()
        .height(530.dp)
        .padding(0.dp)
        .background(color = Color.Transparent)) {
        TextField(
            value = textBoxText.value,
            onValueChange = { newText -> textBoxText.value = newText },
            placeholder = { Text("Enter items in sorted order, one item per line.", color = Color.Gray) },
            colors = TextFieldDefaults.textFieldColors(containerColor = Color.Transparent),
            modifier = Modifier
                .fillMaxSize()
                .padding(16.dp)
                .background(color = Color.Transparent)
        )
    }
}

@Composable
fun ActionButtons() {
    Row (modifier = Modifier
        .fillMaxWidth()
        .padding(16.dp),
        horizontalArrangement = Arrangement.SpaceBetween)
    {

        Button(onClick = {}, shape = RectangleShape,
            colors = ButtonDefaults.buttonColors(containerColor = Color.LightGray, contentColor = Color.Black)) {
            Text(text = "CLEAR")
        }

        Spacer(Modifier.width(6.dp))

        Button(onClick = {}, shape = RectangleShape,
            colors = ButtonDefaults.buttonColors(containerColor = Color.LightGray, contentColor = Color.Black)) {
            Text(text = "NEW GAME")
        }
    }
}