from integrations.elevenlabs_client import ElevenLabsClient
from core.enums import Language

client = ElevenLabsClient()

print("ElevenLabsClient initialized:", type(client))
print("English voice ID:", client.voice_id_en[:8] + "...")
print("Spanish voice ID:", client.voice_id_es[:8] + "...")

en_config = client.build_retell_voice_config(Language.ENGLISH)
es_config = client.build_retell_voice_config(Language.SPANISH)

print("English Retell config built:", en_config["provider"], en_config["model"])
print("Spanish Retell config built:", es_config["provider"], es_config["model"])
print("Voice IDs differ (bilingual):", en_config["voice_id"] != es_config["voice_id"])
print("ElevenLabs client ready")