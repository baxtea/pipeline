import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { Story } from './story';
import { StoryService } from './story.service';

@Component({
  moduleId: module.id,
  selector: 'story-editor',
  templateUrl: 'story-editor.component.html',
  styleUrls: [ 'story-editor.component.css' ]
})
export class StoryEditorComponent implements OnInit {
  stories: Story[];
  selectedStory: Story;

  constructor(
    private router: Router,
    private storyService: StoryService) { }

  getStories(): void {
    this.storyService.getStories().then(stories => this.stories = stories);
  }

  ngOnInit(): void {
    this.getStories();
  }

  onSelect(story: Story): void {
    this.selectedStory = story;
  }
  
  gotoDetail(): void {
    this.router.navigate(['/detail', this.selectedStory.id]);
  }
}
