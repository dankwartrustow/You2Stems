"""
You2Stems
John W. Miller
2020
"""

import sys
import argparse
import warnings

warnings.filterwarnings('ignore')

# TODO: Add option to specify path to downloaded spleeter models


# TODO: Figure out the right way to do this
try:
    # Running from $you2stems in bash
    from you2stems.you2stems import SongToStems
except:
    # Running from a local Python package
    from you2stems import SongToStems


def main(args=None):
    desc = "Download YouTube audio, split the track into instrumental stems."
    parser = argparse.ArgumentParser(
        description=desc,
        prog="you2stems",
        allow_abbrev=False)

    parser.add_argument(
        "url",
        help="The YouTube URL to download audio from.",
        type=str)

    parser.add_argument(
        "--num-stems",
        "-n",
        help="The number of stems to split the audio into.",
        type=int,
        choices=[2, 4, 5],
        default=2)

    parser.add_argument(
        "--download-only",
        "-d",
        help="Only download audio, don't split to stems.",
        type=bool,
        default=False,
        choices=[True, False])

    parser.add_argument(
        "--codec",
        "-c",
        help="Specify the preferred audio codec.",
        type=str.lower,
        choices=["mp3", "wav"],
        default="mp3")

    parser.add_argument(
        "--file",
        "-f",
        help="Specify the save name for the audio file.",
        type=str,
        default=None)

    parser.add_argument(
        "--verbose",
        "-v",
        help="Toggles verbosity.",
        type=bool,
        default=True,
        choices=[True, False])
    args = parser.parse_args()
    print(args)

    # Create the SongToStems instance
    song2stems = SongToStems(
        codec=args.codec,
        num_stems=args.num_stems,
        verbose=args.verbose)

    # If specifid, only download audio then exit
    if args.download_only:
        song2stems.downloader.download_youtube_audio(
            url=args.url,
            filename=args.file)
        return

    # Download audio, split to stems
    song2stems.download_and_split(
        url=args.url,
        filename=args.file)


if __name__ == "__main__":
    main()
    print("Done!")
