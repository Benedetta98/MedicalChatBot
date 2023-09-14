from unittest import result
from telegram import *
from telegram.ext import *
from requests import *
import pandas as pd
import pickle


updater = Updater(token="5221449116:AAFxore3PLVd7vpOPU37JRWzk5eRYlVeRQk")
dispatcher = updater.dispatcher

all_symptoms = ['Dizziness', 'Chest tightness', 'Burning sensation behind the breastbone', 'Chest tightness and shortness of breath', 'Pain behind the breastbone', 'Acid reflux', 'Nausea', 'Vomiting', 'Hard to swallow', 'Stomach ache', 'Bloating', 'Pharynx discomfort', 'Expectoration', 'Cough', 'Fever', 'Palpitations', 'Diarrhea', 'Feel sick and vomit', 'Loss of appetite', 'Hiccup', 'Thin', 'Anorexia', 'Increased stool frequency', 'Edema', 'Constipation', 'Bitter', 'Thirst', 'Hiccough', 'Hemoptysis', 'Twitch', 'Suppuration', 'Chills and fever', 'Black stool', 'Sweating', 'Shortness of breath', 'Poor spirits', 'Poor sleep', 'Stuffy nose', 'Hematemesis', 'Fear of cold', 'Bloody stools', 'Headache', 'Fatigue', 'Dizzy', 'Syncope', 'Consciousness disorder', 'Sleep disorder', 'Body aches', 'Blood in the tears', 'Diplopia', 'Difficulty breathing',
                'Frequent urination', 'Hazy', 'Backache', 'Radiating pain', 'Tensile and heavy', 'Rash', 'Chills', 'Urgency', 'Decreased urine output', 'Abdominal pain and diarrhea', 'Sneeze', 'Cry', 'Waist pain', 'First degree swelling of bilateral tonsils', 'Oliguria', 'Afraid of cold', 'Joint pain', 'Itching', 'Swelling of both nasal mucosa', 'Itchy eyes', 'Ear itching', 'Thin white moss', 'Inspiratory tri-concave sign', 'Tinnitus', 'Vertigo', 'Poor physical activity', 'Pain in front of neck', 'Redness', 'Earache', 'Ulcer', 'Right earache', 'Nose bleeding', 'Nasal mucosal congestion', 'Proptosis', 'Mild thyroid enlargement', 'Afraid of heat', 'Shaking hands', 'Eye swelling', 'Vision loss', 'Head trauma pain', 'Limb numbness', 'Itchy and uncomfortable eyes', 'Jealous', 'Photophobia', 'Papule', 'Dysmenorrhea', 'Breast tenderness', 'Eye pain', 'Lumbago']
data = pd.read_csv("data/new_train_DB.csv")
file_name = 'finalized_model_ovsa.sav'

symptoms = []
df = []

# load trained model
loaded_model_ovsa = pickle.load(open(file_name, 'rb'))


def diagnosis(symptoms):
    df = data[all_symptoms]
    new_row = {}
    keys = symptoms

    for i in keys:
        new_row[i] = '1'
    df = df.append(new_row, ignore_index=True)
    for i in all_symptoms:
        df[i].fillna(-1, inplace=True)
    print(df[-1:])

    result = loaded_model_ovsa.predict(df[-1:])
    return result


def startCommand(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton('Dizziness')], [KeyboardButton('Chest tightness and shortness of breath')],
               [KeyboardButton('Pain behind the breastbone')], [KeyboardButton('Acid reflux')], [
        KeyboardButton('Nausea')], [KeyboardButton('Vomiting')],
        [KeyboardButton('Stomach ache')], [KeyboardButton('Pharynx discomfort')], [
        KeyboardButton('Cough')], [KeyboardButton('Fever')],
        [KeyboardButton('Palpitations')], [KeyboardButton('Diarrhea')], [
        KeyboardButton('Headache')], [KeyboardButton('Rash')],
        [KeyboardButton('Itching')], [KeyboardButton('Breast tenderness')]]
    context.bot.sendPhoto(chat_id=update.effective_chat.id,
                          photo=open('img/profile.jpg', 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm MADDY your personal medical diagnosis system! \nWhat are your symptoms?", reply_markup=ReplyKeyboardMarkup(buttons))


def messageHandler(update: Update, context: CallbackContext):
    if 'Dizziness' in update.message.text:
        buttons = [[KeyboardButton('Nausea')], [KeyboardButton('Headache')],
                   [KeyboardButton('Pain behind the breastbone')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Dizziness')

    if 'Chest tightness and shortness of breath' in update.message.text:
        buttons = [[KeyboardButton('Palpitations')], [KeyboardButton('Breast tenderness')],
                   [KeyboardButton('Pain behind the breastbone')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Chest tightness and shortness of breath')

    if 'Pain behind the breastbone' in update.message.text:
        buttons = [[KeyboardButton('Acid reflux')], [KeyboardButton('Palpitations')],
                   [KeyboardButton('Chest tightness and shortness of breath')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Pain behind the breastbone')

    if 'Acid reflux' in update.message.text:
        buttons = [[KeyboardButton('Nausea')], [KeyboardButton('Stomach ache')],
                   [KeyboardButton('Pain behind the breastbone')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Acid reflux')

    if 'Nausea' in update.message.text:
        buttons = [[KeyboardButton('Stomach ache')], [KeyboardButton('Acid reflux')],
                   [KeyboardButton('Vomiting')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Nausea')

    if 'Vomiting' in update.message.text:
        buttons = [[KeyboardButton('Stomach ache')], [KeyboardButton('Nausea')],
                   [KeyboardButton('Diarrhea')], [KeyboardButton('Other')],   [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Vomiting')

    if 'Stomach ache' in update.message.text:
        buttons = [[KeyboardButton('Acid reflux')], [KeyboardButton('Vomiting')],
                   [KeyboardButton('Diarrhea')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Stomach ache')

    if 'Pharynx discomfort' in update.message.text:
        buttons = [[KeyboardButton('Acid reflux')], [KeyboardButton('Cough')],
                   [KeyboardButton('Fever')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Pharynx discomfort')

    if 'Cough' in update.message.text:
        buttons = [[KeyboardButton('Fever')], [KeyboardButton('Pharynx discomfort')],
                   [KeyboardButton('Chest tightness and shortness of breath')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Cough')

    if 'Fever' in update.message.text:
        buttons = [[KeyboardButton('Pharynx discomfort')], [KeyboardButton('Cough')],
                   [KeyboardButton('Breast tenderness')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Fever')

    if 'Palpitations' in update.message.text:
        buttons = [[KeyboardButton('Chest tightness and shortness of breath')], [KeyboardButton('Cough')],
                   [KeyboardButton('Pain behind the breastbone')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Palpitations')

    if 'Diarrhea' in update.message.text:
        buttons = [[KeyboardButton('Vomiting')], [KeyboardButton('Stomach ache')],
                   [KeyboardButton('Fever')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Diarrhea')

    if 'Headache' in update.message.text:
        buttons = [[KeyboardButton('Breast tenderness')], [KeyboardButton('Fever')],
                   [KeyboardButton('Dizziness')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Headache')

    if 'Rash' in update.message.text:
        buttons = [[KeyboardButton('Itching')], [KeyboardButton('Cough')],
                   [KeyboardButton('Chest tightness and shortness of breath')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Rash')

    if 'Itching' in update.message.text:
        buttons = [[KeyboardButton('Chest tightness and shortness of breath')], [KeyboardButton('Rash')],
                   [KeyboardButton('Fever')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Itching')

    if 'Breast tenderness' in update.message.text:
        buttons = [[KeyboardButton('Chest tightness and shortness of breath')], [KeyboardButton('Fever')],
                   [KeyboardButton('Headache')], [KeyboardButton('Other')], [KeyboardButton('No')]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(
            buttons), text="Other symptoms?")
        symptoms.append('Breast tenderness')

    if 'Other' in update.message.text:
        buttons = [[KeyboardButton('Dizziness')], [KeyboardButton('Chest tightness and shortness of breath')],
                   [KeyboardButton('Pain behind the breastbone')], [KeyboardButton('Acid reflux')], [
            KeyboardButton('Nausea')], [KeyboardButton('Vomiting')],
            [KeyboardButton('Stomach ache')], [KeyboardButton('Pharynx discomfort')], [
            KeyboardButton('Cough')], [KeyboardButton('Fever')],
            [KeyboardButton('Palpitations')], [KeyboardButton('Diarrhea')], [
            KeyboardButton('Headache')], [KeyboardButton('Rash')],
            [KeyboardButton('Itching')], [KeyboardButton('Breast tenderness')]]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="What are your symptoms?", reply_markup=ReplyKeyboardMarkup(buttons))

    if 'No' in update.message.text:
        context.bot.sendPhoto(chat_id=update.effective_chat.id,
                              photo=open('img/result.jpg', 'rb'))
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="I'm thinking...")
        print(symptoms)

        disease = diagnosis(symptoms)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=f'Disease: {disease[0]}')

        buttons = [[InlineKeyboardButton("✅", callback_data="yes")], [
            InlineKeyboardButton("❌", callback_data="no")]]
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(
            buttons), text="Do you want to start another conversation?")


def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data

    if "yes" in query:
        symptoms.clear()
        data.drop(data.columns[-1], axis=1, inplace=True)
        startCommand(update, context)

    if "no" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Bye!")


dispatcher.add_handler(CommandHandler("start", startCommand))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
dispatcher.add_handler(CallbackQueryHandler(queryHandler))

updater.start_polling()
